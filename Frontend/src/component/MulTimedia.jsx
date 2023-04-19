import React, { useState, useEffect } from "react";
import axios from 'axios'

const useAudio = url => {
  const [audio] = useState(new Audio(url));
  const [playing, setPlaying] = useState(false);

  const toggle = () => setPlaying(!playing);

  useEffect(() => {
      playing ? audio.play() : audio.pause();
    },
    [playing]
  );

  useEffect(() => {
    audio.addEventListener('ended', () => setPlaying(false));
    return () => {
      audio.removeEventListener('ended', () => setPlaying(false));
    };
  }, []);

  // useEffect(() => {
  //       axios.get(`http://192.168.1.97:8000/static/t4.wav`)
  //       .then(res => {
  //           console.log(res.data)
  //           const result = res.data;
  //           seturls(result);
  //       })
  //   },[])

  return [playing, toggle];
};

const MulTimedia = ({ url }) => {
  console.log(url)
  const [playing, toggle] = useAudio(url);
  return (
    <div>
      <button onClick={toggle}>{playing ? "Pause" : "Play"}</button>
    </div>
  );
};

export default MulTimedia;
