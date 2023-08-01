import React from 'react';
import './SearchResult.css';

export const SearchResult = ({ city, setLocation, setCities, setInput }) => {

  const handleChange = (e) => {
    setLocation(city);
    setCities([]);
    setInput(city.LocalizedName);
  }

  return (
    <div className='search-result' onClick={ handleChange }>{ city.LocalizedName }</div>
  )
};
