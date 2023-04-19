import React, { useRef } from "react";
import Form from "react-bootstrap/Form";
import FileDetails from "../component/FileDetails/FileDetails";


import useAppContext from "../hooks/useAppContext";

const Upload = () => {
  const inputRef = useRef(null);
  const { setIsUpload ,  setSelectedFile , selectedFile} = useAppContext()

  inputRef.accept = "audio/wav";
  const onFileChange = (event) => {
    setSelectedFile(Array.from(event.target.files));
    setIsUpload(false);
  };



  return (
    <div className="container mt-5">
      <div className="row">
        <div className="d-flex w-100 justify-content-center align-items-center">
          <Form className="w-100">
            <label className="mx-3">Upload only wav file: </label>
            <input
              accept="audio/wav"
              ref={inputRef}
              className="btn btn-warning"
              type="file"
              onChange={onFileChange}
              multiple
            />
            <div className="col-12">
              {selectedFile.length > 0 && (
                <FileDetails inputRef={inputRef}/>
              )}
            </div>

            
          </Form>
        </div>
      </div>
    </div>
  );
};
export default Upload;
