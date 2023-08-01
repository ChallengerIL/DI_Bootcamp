import './Forecast.css';

export const Forecast = ({location, weather, forecast, favorites, setFavorites}) => {

    const weekday = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"];

    const handleFavoritesClick = () => {
        
        if (favorites.length > 0) {
            if (favorites.some(element => element.Key === location.Key)) {
                    setFavorites((oldArray) => [...oldArray].filter(item => item.Key !== location.Key));
            } else {
                setFavorites((oldArray) => [...oldArray, location]);
            }
            
        } else {
            setFavorites((oldArray) => [...oldArray, location]);
        }
        };

    const handleFavoritesCheck = () => {
        return favorites.some(item => item.Key === location.Key);
    }

  return (
    <div className='forecast-card'>
        <div className='upper-row'>
            <i className={handleFavoritesCheck() ? "fa fa-heart favorite" : "fa fa-heart regular"} onClick={ handleFavoritesClick }></i>
            <img src={`https://apidev.accuweather.com/developers/Media/Default/WeatherIcons/${weather.WeatherIcon < 10 ? 0: ''}${weather.WeatherIcon}-s.png`} alt={ weather.WeatherText } />
            <div className='name-temp-container'>
                <p className='city-name'>{ location.LocalizedName }</p>
                <p className='current-temperature'>{ weather.Temperature.Metric.Value }{ weather.Temperature.Metric.Unit }</p>
            </div>
        </div>
        
        <p className='current-conditions'>{ weather.WeatherText }</p>

        <div className='forecast-columns'>
            {forecast.DailyForecasts.map((info, id) => {
                return (
                    <div key={id} className='forecast-columns-card'>
                        <p className='day'>{weekday[(new Date(info.EpochDate * 1000)).getDay()]}</p>
                        <p className='date'>{(new Date(info.EpochDate * 1000)).getMonth()+1}/
                        {(new Date(info.EpochDate * 1000)).getDate()}</p>
                        <img src={`https://apidev.accuweather.com/developers/Media/Default/WeatherIcons/${info.Night.Icon < 10 ? 0: ''}${info.Night.Icon}-s.png`} alt={ info.Night.Icon } />
                        <p className='temperature'>{ info.Temperature.Minimum.Value }{ info.Temperature.Minimum.Unit }</p>
                        <img src={`https://apidev.accuweather.com/developers/Media/Default/WeatherIcons/${info.Day.Icon < 10 ? 0: ''}${info.Day.Icon}-s.png`} alt={ info.Day.Icon } />
                        <p className='temperature'>{ info.Temperature.Maximum.Value }{ info.Temperature.Maximum.Unit }</p>
                    </div>
                )
            })}
        </div>
    </div>
  )
}
