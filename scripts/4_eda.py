import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

DB_FILE = "cricsheet.db"

def load_matches():
    conn = sqlite3.connect(DB_FILE)
    formats = ["odis", "t20s", "tests"]
    dfs = []
    for fmt in formats:
        table_name = f"matches_{fmt}"
        try:
            df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
            df['format'] = fmt
            dfs.append(df)
        except Exception as e:
            print(f"⚠️ Could not load {table_name}: {e}")
    conn.close()
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()

def detect_columns(df):
    batter_col = next((c for c in ['batter','player','batsman'] if c in df.columns), None)
    bowler_col = next((c for c in ['bowler','player'] if c in df.columns), None)
    runs_col = next((c for c in ['runs_total','runs','runs_batsman','score'] if c in df.columns), None)
    wicket_col = next((c for c in ['wicket','wickets'] if c in df.columns), None)
    team_col = next((c for c in ['teams','team'] if c in df.columns), None)
    match_col = next((c for c in ['match_id','id'] if c in df.columns), None)
    
    missing = [col for col in [batter_col, bowler_col, runs_col, wicket_col, team_col, match_col] if col is None]
    if missing:
        raise KeyError(f"Could not detect columns: {missing}")
    
    return batter_col, bowler_col, runs_col, wicket_col, team_col, match_col

# ---------------- PLAYER STATS ----------------
def player_stats_graphs(df):
    batter_col, bowler_col, runs_col, wicket_col, _, match_col = detect_columns(df)
    
    # 1️⃣ Total runs (Matplotlib gradient)
    total_runs = df.groupby(batter_col)[runs_col].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    plt.bar(total_runs.index, total_runs.values, color=plt.cm.plasma(range(len(total_runs))))
    plt.title("🔥 Top 10 Players by Total Runs", fontsize=16, fontweight='bold')
    plt.ylabel("Runs")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # 2️⃣ Total wickets (Seaborn muted)
    total_wickets = df.groupby(bowler_col)[wicket_col].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=total_wickets.index, y=total_wickets.values, palette="muted", edgecolor='black')
    plt.title("🎯 Top 10 Bowlers by Wickets", fontsize=16, fontweight='bold')
    plt.ylabel("Wickets")
    plt.xticks(rotation=45)
    plt.show()

    # 3️⃣ Batting average (Plotly interactive)
    batting_avg = df.groupby(batter_col).agg(total_runs=(runs_col,'sum'), matches=(match_col,'nunique'))
    batting_avg['avg_runs'] = batting_avg['total_runs'] / batting_avg['matches']
    fig = px.bar(batting_avg.sort_values('avg_runs', ascending=False).head(10).reset_index(),
                 x=batter_col, y='avg_runs', color='avg_runs', color_continuous_scale='Blues',
                 title="⭐ Top 10 Batting Averages")
    fig.update_layout(yaxis_title='Average Runs', xaxis_title='Player')
    fig.show()

    # 4️⃣ Matches played (Matplotlib hatch)
    matches_played = df.groupby(batter_col)[match_col].nunique().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    plt.bar(matches_played.index, matches_played.values, color='orange', hatch='//')
    plt.title("🏆 Top 10 Players by Matches Played", fontsize=16, fontweight='bold')
    plt.ylabel("Matches")
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    plt.show()

# ---------------- TEAM INSIGHTS ----------------
def team_insights_graphs(df):
    _, _, runs_col, wicket_col, team_col, match_col = detect_columns(df)

    # 1️⃣ Total runs (Matplotlib rainbow)
    team_runs = df.groupby(team_col)[runs_col].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    plt.bar(team_runs.index, team_runs.values, color=plt.cm.rainbow(range(len(team_runs))))
    plt.title("🔥 Top 10 Teams by Runs", fontsize=16, fontweight='bold')
    plt.ylabel("Runs")
    plt.xticks(rotation=45)
    plt.show()

    # 2️⃣ Total wickets (Seaborn deep)
    team_wickets = df.groupby(team_col)[wicket_col].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=team_wickets.index, y=team_wickets.values, palette="deep", edgecolor='black')
    plt.title("🎯 Top 10 Teams by Wickets", fontsize=16, fontweight='bold')
    plt.ylabel("Wickets")
    plt.xticks(rotation=45)
    plt.show()

    # 3️⃣ Matches played (Matplotlib gradient)
    team_matches = df.groupby(team_col)[match_col].nunique()
    top_matches = team_matches.sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    plt.bar(top_matches.index, top_matches.values, color=plt.cm.cividis(range(10)))
    plt.title("📊 Top 10 Teams by Matches Played", fontsize=16, fontweight='bold')
    plt.ylabel("Matches")
    plt.xticks(rotation=45)
    plt.show()

    # 4️⃣ Pie chart: runs contribution (Matplotlib)
    top_team_runs = df.groupby(team_col)[runs_col].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(8,8))
    plt.pie(top_team_runs.values, labels=top_team_runs.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.tab20.colors)
    plt.title("🏅 Run Contribution by Top 10 Teams", fontsize=16, fontweight='bold')
    plt.show()

# ---------------- FORMAT ANALYSIS ----------------
def format_analysis_graphs(df):
    _, _, runs_col, wicket_col, _, match_col = detect_columns(df)

    # 1️⃣ Total matches (Matplotlib)
    matches_fmt = df.groupby('format')[match_col].nunique()
    plt.figure(figsize=(8,5))
    plt.bar(matches_fmt.index, matches_fmt.values, color='orange')
    plt.title("📌 Total Matches per Format", fontsize=14, fontweight='bold')
    plt.ylabel("Matches")
    plt.show()

    # 2️⃣ Total runs (Seaborn)
    runs_fmt = df.groupby('format')[runs_col].sum()
    plt.figure(figsize=(8,5))
    sns.barplot(x=runs_fmt.index, y=runs_fmt.values, palette="pastel")
    plt.title("📈 Total Runs per Format", fontsize=14, fontweight='bold')
    plt.ylabel("Runs")
    plt.show()

    # 3️⃣ Avg runs per match (Matplotlib gradient)
    avg_runs = df.groupby('format').agg(total_runs=(runs_col,'sum'), matches=(match_col,'nunique'))
    avg_runs['avg_runs'] = avg_runs['total_runs'] / avg_runs['matches']
    plt.figure(figsize=(8,5))
    plt.bar(avg_runs.index, avg_runs['avg_runs'], color=plt.cm.magma(range(len(avg_runs))))
    plt.title("🔥 Avg Runs per Match per Format", fontsize=14, fontweight='bold')
    plt.ylabel("Avg Runs")
    plt.show()

    # 4️⃣ Total wickets (Seaborn)
    wickets_fmt = df.groupby('format')[wicket_col].sum()
    plt.figure(figsize=(8,5))
    sns.barplot(x=wickets_fmt.index, y=wickets_fmt.values, palette="Reds_r")
    plt.title("🎯 Total Wickets per Format", fontsize=14, fontweight='bold')
    plt.ylabel("Wickets")
    plt.show()

# ---------------- RUN ALL ----------------
if __name__ == "__main__":
    df = load_matches()
    if df.empty:
        print("⚠️ No match data loaded.")
    else:
        print("✅ Data loaded successfully.")
        player_stats_graphs(df)
        team_insights_graphs(df)
        format_analysis_graphs(df)
