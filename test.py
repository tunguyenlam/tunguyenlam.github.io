from plotly.subplots import make_subplots
import math


def subplot_by_year(df, month=None, day=None):
    years = df.start_date_year.unique()
    n_items = len(years)
    n = int(math.sqrt(n_items))
    m = n + 1 if math.sqrt(n_items) > n else n

    fig = make_subplots(rows=2, cols=2)
    layout = go.Layout(
        title='trips',
        xaxis=dict(title='Start Date', tickformat='%Y-%m-%d %H:%M:%S'),
        yaxis=dict(title='End Date', tickformat='%Y-%m-%d %H:%M:%S'),
    )
    for i in range(n):
        for j in range(m):
            loc = i * n + j
            year = years[loc]
            plot_df = df[(df['start_date_year'] == year)]
            if month is not None:
                plot_df = plot_df[(plot_df['start_date_month'] == month)]
            if day is not None:
                plot_df = plot_df[(plot_df['start_date_day'] == day)]

            one_date_plot_data = go.Scatter(
                x=plot_df['start_date'],
                y=plot_df['end_date'],
                mode='markers',
                marker_size=plot_df['duration_sec'] / 50,
                marker_color=['rgb(93, 164, 214)', 'rgb(255, 144, 14)', 'rgb(44, 160, 101)', 'rgb(255, 65, 54)']
            )

            fig.append_trace(one_date_plot_data, row=i + 1, col=j + 1)

    fig.show()

import seaborn as sns
sns.distplot(main_trip_df['trip_time_point'])