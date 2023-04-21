import { createContext , useState } from "react";


const AppContext = createContext({
    isUpload:false,
    setIsUpload:() => {},
    selectedFile:[],
    setSelectedFile:() => {},
    dataFromML:null,
    setDataFromML:() => {}
});

const AppContextProvider = ({children}) => {
    const [isUpload , setIsUpload] = useState(false)
    const [selectedFile , setSelectedFile] = useState([]);
    const [dataFromML , setDataFromML] = useState(null)
    const value = { isUpload , setIsUpload , selectedFile , setSelectedFile , dataFromML , setDataFromML}

    return <AppContext.Provider value={value}>{children}</AppContext.Provider>
}

export { AppContext , AppContextProvider }