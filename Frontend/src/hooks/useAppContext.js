import { useContext } from "react";

import { AppContext } from "../context";

const useAppContext = () => {
    const { isUpload , setIsUpload , selectedFile , setSelectedFile } = useContext(AppContext);
    return { isUpload , setIsUpload , selectedFile , setSelectedFile}
}

export default useAppContext;