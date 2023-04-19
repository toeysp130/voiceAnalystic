
import "./App.css";
import Nav from "./component/Nav";
import Upload from "./component/Upload";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {

  return (
    <div>
      <Nav />
      <div className="container">
        <div className="row">
          <div className="col-12">
            <Upload/>
          </div>
          
          <div className="col-6 mt-4">{/* <ShowGet /> */}</div>
        </div>

        {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
      </div>
    </div>
  );
}

export default App;
