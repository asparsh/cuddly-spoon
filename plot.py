from plotly.offline import plot, iplot
import plotly.graph_objs as go#visualization

def plot_details(neg, pos):
    trace1 = {
      "meta": {"columnNames": {
          "x": "0, x",
          "y": "0, y; 1, y"
        }},
      "name": "not_connecteed",
      "text": "",
      "type": "bar",
      "x": neg[1],
      "y": neg[0],
      "marker": {
        "line": {
          "color": "rgba(255, 153, 51, 1.0)",
          "width": 0
        },
        "color": "rgba(0, 192, 255, 0.6)"
      },
      "orientation": "h"
    }
    trace2 = {
      "meta": {"columnNames": {
          "x": "1, x",
          "y": "0, y; 1, y"
        }},
      "name": "connected",
      "text": "",
      "type": "bar",
      "x": pos[1],
      "y": pos[0],
      "marker": {
        "line": {
          "color": "rgba(55, 128, 191, 1.0)",
          "width": 0
        },
        "color": "rgba(123, 3, 207, 0.6)"
      },
      "orientation": "h"
    }
    data = go.Data([trace1, trace2])
    layout = {
      "font": {
        "size": 13,
        "family": "Droid Sans"
      },
      "title": {
        "font": {
          "size": 22,
          "color": "#4D5663",
          "family": "Raleway"
        },
        "text": "Mean Coefficients of LIME explanations by class"
      },
      "xaxis": {
        "type": "linear",
        "range": [-0.10590789156376533, 0.2532052588409005],
        "title": {
          "font": {"color": "#4D5663"},
          "text": "Mean Coefficients from LIME explanations"
        },
        "domain": [0.125, 1],
        "showgrid": True,
        "tickfont": {"color": "#4D5663"},
        "autorange": True,
        "gridcolor": "#E1E5ED",
        "zerolinecolor": "#E1E5ED"
      },
      "yaxis": {
        "type": "category",
        "range": [-0.5, 24.5],
        "title": {
          "font": {"color": "#4D5663"},
          "text": ""
        },
        "domain": [0, 1],
        "showgrid": True,
        "tickfont": {"color": "#4D5663"},
        "autorange": True,
        "gridcolor": "#E1E5ED",
        "zerolinecolor": "#E1E5ED"
      },
      "bargap": 0,
      "legend": {
        "font": {"color": "#4D5663"},
        "bgcolor": "#F5F6F9"
      },
      "barmode": "relative",
      "autosize": True,
      "bargroupgap": 0.28,
      "plot_bgcolor": "#F5F6F9",
      "paper_bgcolor": "#F5F6F9"
    }
    fig = go.Figure(data=data, layout=layout)
    iplot(fig)