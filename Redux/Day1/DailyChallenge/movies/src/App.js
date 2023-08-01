import './App.css';
import MovieList from './components/MovieList';
import MovieDetails from './components/MovieDetails';

function App() {
  return (
    <main>
      <h1>Redux Movies</h1>
      
      <div className='container'>
        <div>
          <MovieList />
        </div>
        <div>
          <MovieDetails />
        </div>
      </div>
    </main>
  );
}

export default App;
