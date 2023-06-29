import './App.css';
import UserFavoriteColors from './FavColors';
import Exercise4 from './Exercise4';

function App() {
  const user = {
    firstName: 'Bob',
    lastName: 'Dylan',
    favAnimals : ['Horse','Turtle','Elephant','Monkey']
  };
  
  return (
    <div>
      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      <ul>
        <UserFavoriteColors favAnimals={user.favAnimals} />
      </ul>
      <Exercise4 />
    </div>
  );
}

export default App;
