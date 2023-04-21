import { useContext } from "react";

import { AppContext } from "../context";

const useAppContext = () => {
    const { isUpload , setIsUpload , selectedFile , setSelectedFile , dataFromML , setDataFromML } = useContext(AppContext);
    return { isUpload , setIsUpload , selectedFile , setSelectedFile , dataFromML , setDataFromML}
}

export default useAppContext;