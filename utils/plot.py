import altair as alt
import pandas as pd
def macro_plot(df, goal_df,plot_width=200):
    chart1 = alt.Chart(df[df['cat']=='calories']).mark_bar().encode(
        alt.Y('cat', title='Calories', axis=alt.Axis(labels=False, ticks=False, titleAngle=0, titlePadding=40)),
        alt.X('value', title='', axis=alt.Axis(values=df.loc[df['cat']=='calories']['value'].to_list()+ \
            goal_df.loc[goal_df['cat']=='calories']['value'].to_list(),
        ticks=False)),
    ).properties(
        width=plot_width,
        height=30) 

    tick1 = alt.Chart(goal_df[goal_df['cat']=='calories']).mark_tick(
        color='red',
        thickness=2,
        size=40 * 0.9,  # controls width of the tick.
    ).encode(
        alt.X('value'),
        alt.Y('cat')
    )

    chart2 = alt.Chart(df[df['cat']=='protein']).mark_bar().encode(
        alt.Y('cat', title='Protein', axis=alt.Axis(labels=False, ticks=False, titleAngle=0, titlePadding=40)),
        alt.X('value', title='', axis=alt.Axis(values=df.loc[df['cat']=='protein']['value'].to_list()+ \
            goal_df.loc[goal_df['cat']=='protein']['value'].to_list(),
        ticks=False)),
    ).properties(
        width=plot_width,
        height=30)

    tick2 = alt.Chart(goal_df[goal_df['cat']=='protein']).mark_tick(
        color='red',
        thickness=2,
        size=40 * 0.9,  # controls width of tick.
    ).encode(
        alt.X('value'),
        alt.Y('cat')
    )

    chart3 = alt.Chart(df[df['cat']=='carb']).mark_bar().encode(
        alt.Y('cat', title='Carb', axis=alt.Axis(labels=False, ticks=False, titleAngle=0, titlePadding=40)),
        alt.X('value',  title='', axis=alt.Axis(values=df.loc[df['cat']=='carb']['value'].to_list()+ \
            goal_df.loc[goal_df['cat']=='carb']['value'].to_list(),
        ticks=False)),
    ).properties(
        width=plot_width,
        height=30)

    tick3 = alt.Chart(goal_df[goal_df['cat']=='carb']).mark_tick(
        color='red',
        thickness=2,
        size=40 * 0.9,  # controls width of tick.
    ).encode(
        alt.X('value'),
        alt.Y('cat')
    )

    chart4 = alt.Chart(df[df['cat']=='fat']).mark_bar().encode(
        alt.Y('cat', title='Fat', axis=alt.Axis(labels=False, ticks=False, titleAngle=0, titlePadding=40)),
        alt.X('value',  title='', axis=alt.Axis(values=df.loc[df['cat']=='fat']['value'].to_list()+ \
            goal_df.loc[goal_df['cat']=='fat']['value'].to_list(),
        ticks=False)),
    ).properties(
        width = plot_width,
        height= 30)

    tick4 = alt.Chart(goal_df[goal_df['cat']=='fat']).mark_tick(
        color='red',
        thickness=2,
        size=40 * 0.9,  # controls width of tick.
    ).encode(
        alt.X('value'),
        alt.Y('cat')
    )

    plot = alt.vconcat(chart1+tick1,chart2+tick2,chart3+tick3, chart4+tick4)
    return plot
