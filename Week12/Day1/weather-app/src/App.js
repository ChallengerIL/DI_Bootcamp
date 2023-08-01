import './App.css';
import { BrowserRouter, Routes, Route, NavLink, redirect } from "react-router-dom";
import HomeScreen from './pages/home';
import FavoritesScreen from './pages/favorites';
import { useState } from 'react';

function App() {

  const [favorites, setFavorites] = useState([]);
  const [location, setLocation] = useState([]);

  return (
    <BrowserRouter>
      <nav className="navbar">
        <ul className="first-list">
          <li className="nav-item">
            <NavLink className="nav-link" to="/">Weather Forecast</NavLink>
          </li>
        </ul>
        <ul className="second-list"><li className="nav-item">
            <NavLink className="nav-link" to="/">Home</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/favorites">Favorites</NavLink>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<HomeScreen setFavorites={ setFavorites } favorites={ favorites } location={ location } setLocation={ setLocation } />} />
        <Route path="/favorites" element={<FavoritesScreen setFavorites={ setFavorites } favorites={ favorites } location={ location } setLocation={ setLocation } />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
