import React, { useEffect, useState } from "react";
import { ScaleLoader } from "react-spinners";
import { getResult } from "../connecter";
const ShowGet = () => {

  const [Result, setResult] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  useEffect(() => {
    setIsLoading(true);

    const fetchData = async() => {
        const result = await getResult(Object.id);
        console.log(result)
        setResult(result);
        setIsLoading(false);
    }
    
    fetchData();
  }, []);

  return (
    <div>
      {/* <ul>
        {isLoading ? (
          <ScaleLoader color="#36d7b7" loading={isLoading} />
        ) : (
          Result.map(({ speaker, transcript }) => (
            <li key={transcript}>
              {" "}
              {speaker} : {transcript}{" "}
            </li>
          ))
        )}
      </ul> */}
    </div>
  );
};
export default ShowGet;
