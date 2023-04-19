import axios from "axios";

const API_URL = "http://192.168.1.11:8000/api/File/";

const getResult = async (id) => {
  try {
    console.log(id)
  // let id = 364
    const result = await axios.get(`${API_URL}${id}`)
    console.log(result)
  } catch (error) {
    console.error(error)
  }
 
  // return result;
};

const postFile = async (files) => {
  return Promise.all(files.map(async (file) => {
    try {
      const formData = new FormData();
      formData.append("file", file);
      const result = await axios.post(API_URL, formData, {
        // const percentCompleted = Math.round(
        //   (pregressEvent.loaded * 100) / pregressEvent.total
        // )
        "Content-Type": "application/form-data",
      });
      console.log(result.data)
      return result;
      // .then(response => {
      // ShowGet(response)
      // setSelectedFile([]);
      // inputRef.current.value = "";
    } catch (error) {
      console.log(error.message);
    }
  }));
};
export { getResult, postFile };
