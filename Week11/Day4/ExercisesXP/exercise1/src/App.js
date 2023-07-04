import './App.css';
import ErrorBoundary from './ErrorBoundary';
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Routes, Route, NavLink } from "react-router-dom";
import { Component } from 'react';

class HomeScreen extends Component {
  render() {
    return(
      <ErrorBoundary>
        <h1>Home</h1>
      </ErrorBoundary>
    );
  };
};

class ProfileScreen extends Component {
  render() {
    return(
      <ErrorBoundary>
        <h1>Profile Screen</h1>
      </ErrorBoundary>
    );
  };
};

class ShopScreen extends Component {
  ThrowError = () => {
    throw new Error('Error during render');
  };

  render() {
    return(
      <ErrorBoundary>
        <this.ThrowError />
      </ErrorBoundary>
    );
  };
};

function App() {
  return (
    <BrowserRouter>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <ul className="nav nav-pills">
          <li className="nav-item">
            <NavLink className="nav-link" to="/">Home</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/profile">Profile</NavLink>
          </li>
          <li className="nav-item">
            <NavLink className="nav-link" to="/shop">Shop</NavLink>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<HomeScreen />} />
        <Route path="/profile" element={<ProfileScreen />} />
        <Route path="/shop" element={<ShopScreen />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
