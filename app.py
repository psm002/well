import streamlit as st

from database import get_well
from plotting import plot_wells

def app():
    st.title('Wells in the US')
    st.markdown('Select the minimum depth and gradient to display:')
    
    min_depth = st.sidebar.number_input('Min depth', 0, 10000, step=500, value=5000)
    min_gradient = st.sidebar.number_input('Min gradient', 0., 0.1, value=0.01, format='%0.3f', step=0.001)
    
    data = get_well(min_depth, min_gradient)
    st.write(plot_wells(data))
    
if __name__ == '__main__':
    app()
