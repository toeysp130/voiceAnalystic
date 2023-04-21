import React , { useState } from "react";
import Swal from 'sweetalert2';

import { postFile } from "../../connecter";
import useAppContext from '../../hooks/useAppContext';

import Analyis_detail from "../Analyis_detail";
import TableUpload from "../TableUpload"
import PopOver from "../PopOver";
import ShowGet from "../ShowGet";


const FileDetails = ({ inputRef }) => {

  const [show, setShow] = useState(false);
  const [idx, set_Idx] = useState(-1);

  const handleClose = () => setShow(false);
  const handleShow = (idx) => {
    setShow(true) 
    set_Idx(idx)
  } 

  const { setIsUpload , selectedFile , setDataFromML } = useAppContext()

  const onFileUpload = async (event) => {
    event.preventDefault();
    const result = await postFile(selectedFile)
    setDataFromML(result.map(data => ({...data.data , res: JSON.parse(data.data.res)})))
    const isSuccess = result.every(data => data.status === 201);
    
    const successSwalOptions = {
      icon:'success',
      title:"Successfully upload files"
    }

    if(isSuccess) setIsUpload(true);

    const errorSwalOptions = {
      icon:'error',
      title:'Something wen\'t wrong , Please try again later'
    }
 
    // ShowGet(result.data.id);
    inputRef.current.value = "";

    Swal.fire(isSuccess ? successSwalOptions : errorSwalOptions)

  };

  return (
    <div>
      <h2>File Details:</h2>
      <div className="position-relative w-full d-block">
        <table className="table table-hover table-striped">
          <thead>
            <tr>
              <th>No.</th>
              <th>Name</th>
              <th>File size</th>
              <th>Created</th>
              <th></th>
              <th>View Detail</th>
            </tr>
          </thead>
          <tbody>
            {
              selectedFile.length > 0 && 
                selectedFile.map((file, index) => (
                  <TableUpload file={file} index={index} key={index} handleShow={handleShow}/>
                )
              )


              
            }
            <tr>
              <td align="right" colSpan={6}>
                <button
                  className="btn btn-outline-primary"
                  onClick={onFileUpload}
                >
                  Upload
                </button>
              </td>
            </tr>
          </tbody>
        </table>

        {/* <MulTimedia url={selectedFile}/> */}
      </div>
      <PopOver isShow={show} hide={handleClose} idx={idx} />
      {/* <Analyis_detail /> */}
    </div>
  );
};

export default FileDetails;
