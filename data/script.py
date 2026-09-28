import pandas as pd
import matplotlib.pyplot as plt

CHEMIN = "data/maroc_croissance.csv"
df = pd.read_csv(CHEMIN)
print(df.head())

periode1 = df[(df["annee"] >= 2000) & (df["annee"] <= 2008)]
periode2 = df[(df["annee"] >= 2015) & (df["annee"] <= 2025)]
inv1 = periode1["investissement_pct_pib"].mean()
cr1 = periode1["croissance_pib_pct"].mean()
inv2 = periode2["investissement_pct_pib"].mean()
cr2 = periode2["croissance_pib_pct"].mean()
print(f"2000-2008 : investissement {inv1:.1f} % | croissance {cr1:.1f} % | ICOR {inv1/cr1:.1f}")
print(f"2015-2025 : investissement {inv2:.1f} % | croissance {cr2:.1f} % | ICOR {inv2/cr2:.1f}")
print("ecart-type 2000-2008:", round(periode1["croissance_pib_pct"].std(), 2),
      "| 2015-2025:", round(periode2["croissance_pib_pct"].std(), 2))

fig, ax1 = plt.subplots(figsize=(11, 6))
ax1.bar(df["annee"], df["investissement_pct_pib"], color="lightsteelblue", label="Investissement (% du PIB)")
ax1.set_xlabel("Année")
ax1.set_ylabel("Investissement (% du PIB)")
ax2 = ax1.twinx()
ax2.plot(df["annee"], df["croissance_pib_pct"], color="darkred", marker="o", label="Croissance du PIB (%)")
ax2.axhline(0, color="gray", linewidth=0.8)
ax2.set_ylabel("Croissance du PIB (%)")
plt.title("Maroc : un investissement élevé pour une croissance faible et instable")
fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.06), ncol=2)
plt.savefig("graphique_1.png", dpi=150, bbox_inches="tight")

periodes = ["2000-2008", "2015-2025"]
x = [0, 1]
largeur = 0.35
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar([i - largeur/2 for i in x], [inv1, inv2], largeur, color="lightsteelblue", label="Investissement moyen (% du PIB)")
ax.bar([i + largeur/2 for i in x], [cr1, cr2], largeur, color="darkred", label="Croissance moyenne (%)")
for i, v in zip([i - largeur/2 for i in x], [inv1, inv2]):
    ax.text(i, v + 0.4, f"{v:.1f} %", ha="center")
for i, v in zip([i + largeur/2 for i in x], [cr1, cr2]):
    ax.text(i, v + 0.4, f"{v:.1f} %", ha="center")
ax.set_xticks(x)
ax.set_xticklabels(periodes)
ax.set_ylabel("%")
ax.set_ylim(0, 38)
ax.set_title("Plus d'investissement, moins de croissance")
ax.legend(loc="upper center", ncol=2)
plt.savefig("graphique_2.png", dpi=150, bbox_inches="tight")
plt.show()
