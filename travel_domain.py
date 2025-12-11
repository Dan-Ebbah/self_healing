from domain import DataType, Action, Domain

TripRequest = DataType("TripRequest")
UserProfile = DataType("UserProfile")
FlightSearchParams = DataType("FlightSearchParams")
FlightOptions = DataType("FlightOptions")
SelectedFlight = DataType("SelectedFlight")
HotelSearchParams = DataType("HotelSearchParams")
HotelOptions = DataType("HotelOptions")
SelectedHotel = DataType("SelectedHotel")
PaymentInfo = DataType("PaymentInfo")
PaymentAuthorization = DataType("PaymentAuthorization")
FlightBooking = DataType("FlightBooking")
HotelBooking = DataType("HotelBooking")
Itinerary = DataType("Itinerary")
WeatherSearchParams = DataType("WeatherSearchParams")
WeatherReport = DataType("WeatherReport")

def build_travel_domain() -> Domain:
    search_flights_A = Action(
        name="search_flights_A",
        preconditions={FlightSearchParams},
        effects={FlightOptions},
        impl=None,
    )

    search_flights_B = Action(
        name="search_flights_B",
        preconditions={FlightSearchParams},
        effects={FlightOptions},
        impl=None,
    )

    book_flights_A = Action(
        name="book_flights_A",
        preconditions={SelectedFlight, PaymentInfo},
        effects={FlightBooking},
        impl=None,
    )
    book_flights_B = Action(
        name="book_flights_B",
        preconditions={SelectedFlight, PaymentInfo},
        effects={FlightBooking},
        impl=None,
    )
    search_hotels = Action(
        name="search_hotels",
        preconditions={HotelSearchParams},
        effects={HotelOptions},
        impl=None,
    )
    book_hotel = Action(
        name="book_hotel",
        preconditions={SelectedHotel, PaymentInfo},
        effects={HotelBooking},
        impl=None,
    )
    charge_v1 = Action(
        name="charge_v1",
        preconditions={PaymentInfo},
        effects={PaymentAuthorization},
        impl=None,
    )

    make_itinerary = Action(
        name="make_itinerary",
        preconditions={FlightBooking, HotelBooking, TripRequest},
        effects={Itinerary},
        impl=None,
    )

    get_weather_location = Action(
        name="get_weather_location",
        preconditions={WeatherSearchParams},
        effects={WeatherReport},
        impl=None,
    )

    derive_FlightSearchParams_from_TripRequest = Action(
        name="derive_FlightSearchParams_from_TripRequest",
        preconditions={TripRequest},
        effects={FlightSearchParams},
        impl=None,
    )
    derive_HotelSearchParams_from_TripRequest = Action(
        name="derive_HotelSearchParams_from_TripRequest",
        preconditions={TripRequest},
        effects={HotelSearchParams},
        impl=None,
    )
    derive_SelectedFlight_from_FlightOptions = Action(
        name="derive_SelectedFlight_from_FlightOptions",
        preconditions={FlightOptions},
        effects={SelectedFlight},
        impl=None,
    )

    derive_SelectedHotel_from_HotelOptions = Action(
        name="derive_SelectedHotel_from_HotelOptions",
        preconditions={HotelOptions},
        effects={SelectedHotel},
        impl=None,
    )

    derive_WeatherSearchParams_from_TripRequest = Action(
        name="derive_WeatherSearchParams_from_TripRequest",
        preconditions={TripRequest},
        effects={WeatherSearchParams},
        impl=None,
    )


    domain = Domain(
        name="TravelPlanningDomain",
        data_types={
            TripRequest,
            UserProfile,
            FlightSearchParams,
            FlightOptions,
            SelectedFlight,
            HotelSearchParams,
            HotelOptions,
            SelectedHotel,
            PaymentInfo,
            PaymentAuthorization,
            FlightBooking,
            HotelBooking,
            Itinerary,
            WeatherSearchParams,
            WeatherReport,
        },
        actions=[
            search_flights_A,
            search_flights_B,
            book_flights_A,
            book_flights_B,
            search_hotels,
            book_hotel,
            make_itinerary,
            get_weather_location,
            derive_FlightSearchParams_from_TripRequest,
            derive_HotelSearchParams_from_TripRequest,
            derive_SelectedFlight_from_FlightOptions,
            derive_SelectedHotel_from_HotelOptions,
            derive_WeatherSearchParams_from_TripRequest,
        ],
    )

    return domain