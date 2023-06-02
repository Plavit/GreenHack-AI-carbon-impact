import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load data from CSV file
data = pd.read_csv('data/dummy_pie.csv')

# Calculate the count of each category in the data
category_counts = data['Type'].value_counts()

# Create a pie chart using Plotly Express
fig = px.pie(data_frame=data, names=category_counts.index, values=category_counts.values, title='Category Distribution')

# Create the Dash application
app = Dash(__name__)

# Define the layout of the application
app.layout = html.Div(
    children=[
        html.H1('Plotly Pie Chart'),
        dcc.Graph(figure=fig)
    ]
)

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)