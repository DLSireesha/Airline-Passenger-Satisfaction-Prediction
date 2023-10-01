import streamlit as st
import pickle
import pandas as pd
from PIL import Image


model = pickle.load(open('Airline_Satisfaction.pkl', 'rb'))


def predict(input_data):
    # Process the input data and make predictions using your model
    prediction = model.predict(input_data)
    return prediction


def main():
    im=Image.open("airline.jpg")
    
    st.set_page_config(page_title="Airline Passenger Satisfaction App",layout="wide",page_icon = im)
    
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    #footer {visibility: hidden;}
    #</style> """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    [data-testid=stSidebar] {
        background-color: #FFFFFF;
        
    }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        "# Dashboard"
    app_mode=st.sidebar.selectbox("Select Page",["Home","About Dataset","Prediction"])
    
    if(app_mode=="Home"):
        st.markdown("<h1 style='text-align: center; color:black;'>AIRLINE PASSENGER SATISFACTION PREDICTION</h1>", unsafe_allow_html=True)
        st.image("background.jpg")
        st.markdown("<h4>The Airline Passenger Satisfaction Prediction using Random Forest Regression project aims to use machine learning to forecast passenger satisfaction levels based on various aspects of their travel experience. This analysis is crucial for airlines seeking to understand the key factors influencing passenger contentment, enabling them to address potential pain points and enhance overall satisfaction.</h4>",unsafe_allow_html=True)
        st.markdown("<h4>The main goal here is to help airlines figure out what really matters to their customers. When passengers are happy, they're more likely to choose that airline again in the future. So, by identifying and improving the aspects of the travel experience that are most important to passengers, airlines can grow their business and build a strong reputation.</h4>",unsafe_allow_html=True)
        st.markdown("<h4>This project isn't just about numbers and data. It's about making air travel a better and more enjoyable experience for everyone involved. By using these predictions, airlines can focus on what truly matters to their customers, making sure they have a positive experience from the moment they step into the airport until they reach their destination. Ultimately, it's about creating a win-win situation for both passengers and airlines.</h4>",unsafe_allow_html=True)
    
    elif(app_mode=="About Dataset"):
        st.markdown("<h2 style='text-align: center; color: black;'>ABOUT DATASET</h2>", unsafe_allow_html=True)
        st.markdown("<h3>Context:</h3>",unsafe_allow_html=True)
        st.markdown("<h5>The Airline Passenger Satisfaction dataset is a comprehensive collection of customer feedback from passengers. The dataset contains information on various aspects of the passengers’ travel experience, such as flight distance, gender, age, type of travel, class, seat comfort, inflight entertainment, onboard service, cleanliness, departure delay, arrival delay, and overall satisfaction. This dataset aims to provide insights into the factors that contribute to passenger satisfaction and dissatisfaction, which can be used by airlines to improve their services and enhance their customers’ travel experience. It contains the following columns:.</h5>",unsafe_allow_html=True)
        st.markdown("<h6>1.Gender: Gender of the passengers (Female, Male)</h6>",unsafe_allow_html=True) 
        st.markdown("<h6>2.Customer Type: The customer type (Loyal customer, disloyal customer)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>3.Age: The actual age of the passengers</h6>",unsafe_allow_html=True)
        st.markdown("<h6>4.Type of Travel: Purpose of the flight of the passengers (Personal Travel, Business Travel)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>5.Class: Travel class in the plane of the passengers (Business, Eco, Eco Plus)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>6.Flight distance: The flight distance of this journey</h6>",unsafe_allow_html=True)
        st.markdown("<h6>7.Inflight wifi service: Satisfaction level of the inflight wifi service (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>8.Departure/Arrival time convenient: Satisfaction level of Departure/Arrival time convenient (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>9.Ease of Online booking: Satisfaction level of online booking (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>10.Gate location: Satisfaction level of Gate location (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>11.Food and drink: Satisfaction level of Food and drink (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>12.Online boarding: Satisfaction level of online boarding (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>13.Seat comfort: Satisfaction level of Seat comfort (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>14.Inflight entertainment: Satisfaction level of inflight entertainment (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>15.On-board service: Satisfaction level of On-board service (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>16.Leg room service: Satisfaction level of Leg room service (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>17.Baggage handling: Satisfaction level of baggage handling (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>18.Check-in service: Satisfaction level of Check-in service (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>19.Inflight service: Satisfaction level of inflight service (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>20.Cleanliness: Satisfaction level of Cleanliness (0:Not Applicable;1-5)</h6>",unsafe_allow_html=True)
        st.markdown("<h6>21.Departure Delay in Minutes: Minutes delayed when departure</h6>",unsafe_allow_html=True)
        st.markdown("<h6>22.Arrival Delay in Minutes: Minutes delayed when Arrival</h6>",unsafe_allow_html=True)
        st.markdown("<h6>23.Satisfaction: Airline satisfaction level(Satisfaction, neutral or dissatisfaction)</h6>",unsafe_allow_html=True)
        st.write("")
        st.write("Download Dataset From here: [Dataset](https://www.kaggle.com/datasets/teejmahal20/airline-passenger-satisfaction)")
    
    # Create input fields for the required features
    elif(app_mode=="Prediction"):
        st.markdown("<h3 style='text-align: center; color: black;'>Model Prediction</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: black;'>Enter the required details for prediction:</h3>", unsafe_allow_html=True)
        gender = st.selectbox('gender', ['Male', 'Female'])
        customer_type=st.selectbox('Customer Type',['Loyal Customer','Disloyal Customer'])
        Age=st.text_input("Age")
        type_of_travel=st.selectbox('Type of Travel',['Personal Travel','Business Travel'])
        Class=st.selectbox('Class',['Eco','Eco Plus','Business'])
        flight_dist = st.text_input("Flight Distance")
        try:
            flight_dist = float(flight_dist)
        except (ValueError, TypeError):
            flight_dist = 0.0
        wifi=st.radio("Inflight Wifi Service",["0",'1','2','3','4','5'],horizontal=True)
        time=st.radio("Departure/Arrival time convenient",['0','1','2','3','4','5'],horizontal=True)
        online_booking=st.radio("Ease of Online booking",['0','1','2','3','4','5'],horizontal=True)
        gate_location=st.radio("Gate Location",['0','1','2','3','4','5'],horizontal=True)
        food_drink=st.radio("Food and Drink",['0','1','2','3','4','5'],horizontal=True)
        boarding=st.radio("Online Boarding",['0','1','2','3','4','5'],horizontal=True)
        comfort=st.radio("Seat Comfort",['0','1','2','3','4','5'],horizontal=True)
        entertainment=st.radio("Inflight Entertainment",['0','1','2','3','4','5'],horizontal=True)
        on_board_service=st.radio("On_Board Service",['0','1','2','3','4','5'],horizontal=True)
        leg_service=st.radio("Leg Room Service",['0','1','2','3','4','5'],horizontal=True)
        baggage=st.radio("Baggage Handling",['0','1','2','3','4','5'],horizontal=True)
        check_in=st.radio("Check_in Service",['0','1','2','3','4','5'],horizontal=True)
        inflight_service=st.radio("Inflight Service",['0','1','2','3','4','5'],horizontal=True)
        clean=st.radio("Cleanliness",['0','1','2','3','4','5'],horizontal=True)
        departure = st.text_input("Departure Delay in Minutes")
        if departure:
            departure = float(departure)
        arrival = st.text_input("Arrival Delay in Minutes")
        if arrival:
            arrival = float(arrival)
        
        if gender == 'Male':
            gender = 1 
        else:
            gender = 0
            
        if customer_type== 'Loyal Customer':
            customer_type = 0 
        else:
            customer_type=1
        
        if type_of_travel == 'Personal Travel':
            type_of_travel = 1 
        else:
            type_of_travel = 0
            
        if Class== 'Eco':
            Class = 1 
        elif Class == 'Eco Plus':
            Class=2 
        else:
            Class=0
            
        # Create a dictionary of input values
        input_data = {
            'Gender': gender,
            'Customer Type': customer_type,
            'Age': Age,
            'Type of Travel': type_of_travel,
            'Class': Class,
            'Flight Distance': flight_dist,
            'Inflight Wifi Service': wifi,
            'Departure/Arrival time convenient': time,
            'Ease of Online booking': online_booking,
            'Gate Location': gate_location,
            'Food and Drink': food_drink,
            'Online Boarding': boarding,
            'Seat Comfort': comfort,
            'Inflight Entertainment': entertainment,
            'On_Board Service': on_board_service,
            'Leg Room Service': leg_service,
            'Baggage Handling': baggage,
            'Check_in Service': check_in,
            'Gate Location': gate_location,
            'Inflight Service': inflight_service,
            'Cleanliness': clean,
            'Departure Delay in Minutes': departure,
            'Arrival Delay in Minutes': arrival
        }
        
        # Convert input data to a DataFrame
        input_df = pd.DataFrame([input_data])
        # Center the content
        col1, col2, col3 = st.columns(3)
        
        # Add empty columns for centering
        col1.write("")
        col2.write("")
        # Add button in the center column with increased width
        with col2:
            # Apply CSS styling to increase button width
            button_style = "<style>.stButton button {background-color: black;color: white;width: 300px;}</style>"
            st.markdown(button_style, unsafe_allow_html=True)
            if st.button('Predict'):
                prediction=predict(input_df)
                if prediction[0]==1:
                    st.success("PASSENGER SATISFIED")
                else:
                    st.warning("PASSENGER NOT LIKELY TO BE SATISFIED")
        
               

if __name__ == '__main__':
    main()
