import { useState, useEffect } from 'react';
import axios from 'axios';
import apiKey from '../apiKey';
import { SearchResult } from '../components/SearchResult';
import { Forecast } from '../components/Forecast';
import './home.css';
import { useLocation } from "react-router-dom";

const telAvivKey = '215854';
const baseURL = 'http://dataservice.accuweather.com/locations/v1/cities';

export default function HomeScreen({ setFavorites, favorites, location, setLocation }) {
    const [cities, setCities] = useState([]);
    const [weather, setWeather] = useState([]);
    const [forecast, setForecast] = useState([]);
    const [loading, setLoading] = useState(true);
    const [input, setInput] = useState('');

    const locationRouter = useLocation();
    let cityKey;

    if (locationRouter.state) {
        cityKey = locationRouter.state.cityKey;
    }
    

    const makeRequest = async (query) => {
        const response = await axios(`${baseURL}/autocomplete?apikey=${apiKey.apiKey}&q=${query}`);
        setCities(response.data)
    };

    useEffect(() => {
        const getDefaultLocation = async () => {
            const locationKeyResponse = await axios(`http://dataservice.accuweather.com/locations/v1/${telAvivKey}?apikey=${apiKey.apiKey}`);
            setLocation(locationKeyResponse.data);
        }

        if (!cityKey) {
            getDefaultLocation();
        }
      }, []);

    const handleChange = (value) => {
        setInput(value);
        makeRequest(value);
    };

    useEffect(() => {
        async function getForecast() {
            setLoading(true);

            const weatherResponse = await axios(`http://dataservice.accuweather.com/currentconditions/v1/${location.Key}?apikey=${apiKey.apiKey}`);
            setWeather(weatherResponse.data[0]);

            const forecastResponse = await axios(`http://dataservice.accuweather.com/forecasts/v1/daily/5day/${location.Key}?apikey=${apiKey.apiKey}&metric=true`);
            setForecast(forecastResponse.data);

            setLoading(false);
        }

        if (location.Key) {
            getForecast();
        }

      }, [location]);

    if (loading) {
        return <>Loading...</>
    }

    return(
        <>
            <div className='search'>
                <div className="search-input">
                    <input placeholder="Search..." value={input} onChange={(e) => handleChange(e.target.value)} />
                </div>
                <div className='dropdown-list'>
                    {cities ?
                        cities.map((city, id) => {
                            return <SearchResult city={ city } key={ id } setLocation={ setLocation } setCities={ setCities } setInput={ setInput } />
                        }) :
                    <></> 
                    }
                </div>
            </div>
            <div className="container">
                <Forecast location={location} weather={weather} forecast={forecast} favorites={favorites} setFavorites={setFavorites} />
            </div>
        </>
    );
  };
