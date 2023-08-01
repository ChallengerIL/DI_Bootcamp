import { useState } from "react";
import "./SearchBar.css";
import axios from "axios";
import apiKey from '../apiKey';

const baseURL = 'http://dataservice.accuweather.com/locations/v1/cities'

export const SearchBar = ({ setCities }) => {
    const [input, setInput] = useState('');

    const makeRequest = async (query) => {
        const response = await axios(`${baseURL}/autocomplete?apikey=${apiKey.apiKey}&q=${query}`);
        setCities(response.data)
    };

    const handleChange = (value) => {
        setInput(value);
        makeRequest(value);
    };

    return (
        <div className="search-input">
            <input placeholder="Search..." value={input} onChange={(e) => handleChange(e.target.value)} />
        </div>
    );
}

export { baseURL };
