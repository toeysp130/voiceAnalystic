import { createContext , useState } from "react";


const AppContext = createContext({
    isUpload:false,
    setIsUpload:() => {},
    selectedFile:[],
    setSelectedFile:() => {}
});

const AppContextProvider = ({children}) => {
    const [isUpload , setIsUpload] = useState(false)
    const [selectedFile , setSelectedFile] = useState([]);
    const value = { isUpload , setIsUpload , selectedFile , setSelectedFile}

    return <AppContext.Provider value={value}>{children}</AppContext.Provider>
}

export { AppContext , AppContextProvider }