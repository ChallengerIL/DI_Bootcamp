import React from 'react';
import './SearchBar.css';
import { SearchResult } from './SearchResult';
import { useState, useEffect } from 'react';

export const SearchBarDropdown = ({ cities, setCities }) => {

  const [clicked, setClicked] = useState(false);

  useEffect(() => {
    if (cities) {
      if (cities.length > 1) {
        setClicked(false);
      }
    }
  }, [cities]);

  return (
    clicked ? <></> :
    cities ? 
    <div className='dropdown-list'>
        {
            cities.map((city, id) => {
                return <SearchResult city={ city } key={ id } setCities={ setCities } setClicked={ setClicked } />
            })    
        }
    </div> :
    <></>
  )
}
