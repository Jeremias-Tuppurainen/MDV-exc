import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

# BMI = weight(kg) / (height(m))^2  →  overweight if BMI > 25
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(
    lambda x: 1 if x > 25 else 0
)

# 0 = good (value == 1 in original), 1 = bad (value > 1 in original)
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc']        = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

def draw_cat_plot():
    cat_features = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']

    # Melt to long format
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=cat_features
    )

    # Count occurrences
    df_cat = (
        df_cat
        .groupby(['cardio', 'variable', 'value'], as_index=False)
        .size()
        .rename(columns={'size': 'total'})
    )

    # Draw facet catplot
    g = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar',
        order=sorted(cat_features),
        height=5,
        aspect=1.1,
        legend=False
    )
    g.add_legend()
    fig = g.figure

    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # Clean up
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))
    ]

    corr = df_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Draw heatmap
    fig, ax = plt.subplots(figsize=(12, 10))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        linewidths=0.5,
        square=True,
        center=0,
        vmin=-0.16,
        vmax=0.32,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )

    fig.savefig('heatmap.png')
    return fig
