import { useState, useEffect } from 'react';
import axios from "axios";
import apiKey from '../apiKey';
import './favorites.css';
import { useNavigate } from 'react-router-dom';


export default function FavoritesScreen({ setFavorites, favorites, setLocation }) {
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    const navigateHome = (city) => {
        navigate('/', {state: {cityKey: city.Key}});
        setLocation(city);
      };

    async function makeRequest(key, index) {
        const weatherResponse = await axios(`http://dataservice.accuweather.com/currentconditions/v1/${key}?apikey=${apiKey.apiKey}`);

        let newFavoritesArr = [...favorites];
        newFavoritesArr[index] = Object.assign(favorites[index], weatherResponse.data[0]);

        setFavorites(newFavoritesArr);
    }

    useEffect(() => {
        async function getWeather() {
            setLoading(true);

            favorites.map((city, index) => {
                makeRequest(city.Key, index);
            })
            
            setLoading(false);
        }

        getWeather();
      });

    if (loading) {
        return <>Loading...</>
    }

    return(
        <div className="container">
            {favorites.map((city, id) => {
                if (city.Temperature) {
                    return (
                        <div className='favorite-card' key={id} onClick={ () => navigateHome(city) }>
                            <p className='city-name'>{city.LocalizedName}</p>
                            <p>
                                {city.Temperature.Metric.Value}
                                {city.Temperature.Metric.Unit}
                            </p>
                            <p>{city.WeatherText}</p>
                        </div>
                    )
                }
            })
            }
        </div>
    );
  };
