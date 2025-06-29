import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [url, setURL] = useState('');
  const [shortURL, setShortURL] = useState('')
  const BACKEND_URL = import.meta.env.VITE_APP_BACKEND_URL;

  const handleSubmit = async () => {
    if(!url) return 

    const response = await fetch(`${BACKEND_URL}/api/shorten`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        longUrl: url
      })
    });

    const data = await response.json();
    setShortURL(data.short_url)
  };
  

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>bitly</h1>
      <div className="card">
        <input 
          placeholder='Enter a URL'
          value={url}
          onChange={(e) => { setURL(e.target.value); setShortURL('')}}
        />
        <button onClick={handleSubmit}>
          Short the URL
        </button>
        <div className='url-container'>
          {
            shortURL && (
              <a href={`${BACKEND_URL}/api/${shortURL}`} target='_blank'>
                {  BACKEND_URL + '/api/' + shortURL }
              </a>
            )
          }
        </div>
       
      </div>
      <p className="read-the-docs">
        made by sunil
      </p>
    </>
  )
}

export default App
