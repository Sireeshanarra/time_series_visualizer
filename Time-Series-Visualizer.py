import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data with corrected file path
try:
    df = pd.read_csv(r"C:\Python34\fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    print("Data loaded successfully.")
    print(df.head())
except Exception as e:
    print(f"Error loading data: {e}")

# Clean data
try:
    df = df[
        (df['value'] >= df['value'].quantile(0.025)) & 
        (df['value'] <= df['value'].quantile(0.975))
    ]
    print("Data cleaned successfully.")
except Exception as e:
    print(f"Error cleaning data: {e}")

def draw_line_plot():
    try:
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.plot(df.index, df['value'], color='r', linewidth=1)
        ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
        ax.set_xlabel("Date")
        ax.set_ylabel("Page Views")
        plt.xticks(rotation=45)
        plt.show()  # Show plot for interactive environments
        plt.savefig('line_plot.png')
        print("Line plot created successfully.")
        return fig
    except Exception as e:
        print(f"Error creating line plot: {e}")

def draw_bar_plot():
    try:
        df_bar = df.copy()
        df_bar['year'] = df_bar.index.year
        df_bar['month'] = df_bar.index.month
        df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

        fig = df_bar.plot(kind='bar', figsize=(12, 6), legend=True).figure
        plt.xlabel("Years")
        plt.ylabel("Average Page Views")
        plt.legend(title="Months", labels=[
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ])
        plt.xticks(rotation=45)
        plt.show()  # Show plot for interactive environments
        plt.savefig('bar_plot.png')
        print("Bar plot created successfully.")
        return fig
    except Exception as e:
        print(f"Error creating bar plot: {e}")

def draw_box_plot():
    try:
        df_box = df.copy()
        df_box.reset_index(inplace=True)
        df_box['year'] = df_box['date'].dt.year
        df_box['month'] = df_box['date'].dt.strftime('%b')
        df_box['month_num'] = df_box['date'].dt.month
        df_box = df_box.sort_values('month_num')

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
        ax1.set_title("Year-wise Box Plot (Trend)")
        ax1.set_xlabel("Year")
        ax1.set_ylabel("Page Views")

        sns.boxplot(x='month', y='value', data=df_box, ax=ax2)
        ax2.set_title("Month-wise Box Plot (Seasonality)")
        ax2.set_xlabel("Month")
        ax2.set_ylabel("Page Views")

        plt.show()  # Show plot for interactive environments
        plt.savefig('box_plot.png')
        print("Box plots created successfully.")
        return fig
    except Exception as e:
        print(f"Error creating box plot: {e}")

if __name__ == "__main__":
    draw_line_plot()
    draw_bar_plot()
    draw_box_plot()
