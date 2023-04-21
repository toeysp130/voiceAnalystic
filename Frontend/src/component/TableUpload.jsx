import React, { useEffect } from "react";

import useAppContext from "../hooks/useAppContext";

const TableUpload = ({ file, index, handleShow }) => {
  const { isUpload, dataFromML } = useAppContext();
  console.log({dataFromML})


  return (
    <tr>
      <td>{`${index + 1}.`}</td>
      <td>{file.name}</td>
      <td>{file.size * 0.001} KB</td>
      <td>
        {new Date(file.lastModified).toLocaleDateString("en-EN", {
          year: "numeric",
          month: "long",
          day: "numeric",
        })}
      </td>
      <td>
        <audio controls>
          <source src={URL.createObjectURL(file)} />
        </audio>
      </td>
      <td>
        <button
          type="button"
          disabled={!isUpload}
          onClick={async () => {
            handleShow(index);
          }}
          className="btn btn-primary"
        >
          Detail
        </button>
      </td>
    </tr>
  );
};

export default TableUpload;
