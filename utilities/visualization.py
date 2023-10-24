import plotly.express as px
import streamlit as st
import altair as alt
import pandas as pd

def bar_graph(df, x_col, y_col, title, x_label, y_label):
    bar_graph = px.bar(df, x=df[x_col], y=df[y_col], title=title, labels={x_col: x_label, y_col: y_label})
    return (bar_graph)


def line_break():
    st.markdown("<br>", unsafe_allow_html=True)


def pie_chart(df, value, category, title_chart):
    fig = px.pie(df, values=value, names=category, title=title_chart)
    return (fig)


def line_chart(data, x_column, y_column, title=None, x_axis_label=None, y_axis_label=None):

    chart = alt.Chart(data).mark_line().encode(
        x=alt.X(x_column, title=x_axis_label),
        y=alt.Y(y_column, title=y_axis_label)
    ).properties(
        width=400,
        height=300,
        title=title
    )
    return chart