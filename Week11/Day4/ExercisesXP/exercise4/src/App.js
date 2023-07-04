import './App.css';

const url = "https://webhook.site/771e575f-ebb6-46f6-8622-ea3f0150b3c8";

function App() {
  const data = {
    key1: 'myusername',
    email: 'mymail@gmail.com',
    name: 'Isaac',
    lastname: 'Doe',
    age: 27
  };

  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  }; 

  const makePostRequest = async () => {
      const response = await fetch(url, requestOptions);

      console.log(response);
  };
  
  return (
    <>
      <button onClick={makePostRequest}>Press me to post some data</button>
    </>
  );
}

export default App;
