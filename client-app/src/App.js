import './App.css';
import SidebarImages from './components/sidebar-images/sidebar-images';
import SubmitPicture from './components/submit-picture/submit-picture';
import ImageInfo from './components/image-info/image-info'

function App() {
  let endpoint = 'http://localhost:8080';

  return (
    <div className="App">
      Hello, world !
      <div className='components'> 
        <SidebarImages url={endpoint} />
        <SubmitPicture url={endpoint} />
        <ImageInfo />
      </div>
    </div>
  );
}

export default App;
