import matplotlib.pyplot as plt

def plot_skill_charts(matched_skills, missing_skills, pie_path="static/pie_chart.png", bar_path="static/bar_chart.png"):
    # PIE CHART
    labels = ['Matched', 'Missing']
    sizes = [len(matched_skills), len(missing_skills)]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    plt.tight_layout()
    plt.savefig(pie_path)
    plt.close(fig1)

    # BAR CHART
    labels_bar = matched_skills + missing_skills
    values = [1]*len(matched_skills) + [0]*len(missing_skills)
    colors = ['green']*len(matched_skills) + ['red']*len(missing_skills)

    fig2, ax2 = plt.subplots(figsize=(10, 4))
    ax2.barh(labels_bar, values, color=colors)
    ax2.set_xlabel("Skill Match (1 = Matched, 0 = Missing)")
    ax2.set_title("Individual Skill Match")
    plt.tight_layout()
    plt.savefig(bar_path)
    plt.close(fig2)
