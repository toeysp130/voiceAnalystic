import React, { useState, useEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Table from 'react-bootstrap/Table';

import Dchart from './Dchart';
import Container from 'react-bootstrap/Container'
import ShowGet from './ShowGet';
import useAppContext from "../hooks/useAppContext";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const PopOver = ({isShow , hide, idx}) => {
  const { dataFromML } = useAppContext();
  const [data_ML, setData_ML] = useState(null)

  const [dataChart, setDataChart] = useState({ pos: 0, neu: 0, neg: 0 })
  
  const processDataChart = () => {
    console.log('data_ML in processDataChart', data_ML)
    if (data_ML === null) return

    let data_ML_res = data_ML.res
    let tmpDataChart = { pos: 0, neu: 0, neg: 0 }

    data_ML_res.forEach(item => {
      let Sentiment_JSON = JSON.parse(item.Sentiment)
      tmpDataChart.pos += Sentiment_JSON.pos
      tmpDataChart.neu += Sentiment_JSON.neu
      tmpDataChart.neg += Sentiment_JSON.neg
    })

    tmpDataChart.neg = tmpDataChart.neg / data_ML_res.length
    tmpDataChart.pos = tmpDataChart.pos / data_ML_res.length
    tmpDataChart.neu = tmpDataChart.neu / data_ML_res.length

    console.log('tmpDataChart = ', tmpDataChart)
    setDataChart(tmpDataChart)
    
  }


  useEffect(() => {
    processDataChart()
  }, [data_ML])

  
  useEffect(() => {
    console.log('index ', idx)
    if (idx !== -1) {
      setData_ML(dataFromML[idx])
    }
  }, [dataFromML, idx])

  return (
    <Modal show={isShow} onHide={hide} size={"xl"}>
        <Modal.Header closeButton>
          <Modal.Title>RegularX & Sentiment Result</Modal.Title>
        </Modal.Header>
        <Modal.Body>
            <Container>
              <Row> 
                <Col lg={4}>
                  <Row>
                    <Dchart sentiment={dataChart} />
                  </Row>
                  <Row>
                    <Table striped="columns">
                      <thead>
                        <tr>
                          <th> Match Intent</th>
                          <th></th>
                        </tr>
                      </thead>
                      <tbody>
                        {
                          data_ML !== null &&
                          data_ML.res.map((item, index) => {
                            
                            let regular = JSON.parse(item.RegularExpression)
                            
                            if (regular.length !== 0) {
                              return (
                                <tr key={index}>
                                  <td>
                                    { regular[0] }
                                  </td>
                                  <td>
                                    { regular[1] }
                                  </td>
                                </tr>
                              )
                            }
                          })
                        }
                      </tbody>
                    </Table>
                  </Row>
                </Col>
                <Col lg={8}>
                  <Table striped="columns">
                    <thead>
                      <tr>
                        <th>SpeakerLabel</th>
                        <th>StartTime</th>
                        <th>EndTime</th>
                        <th>TimeSeconds</th>
                        <th>Transcription</th>

                      </tr>

                      
                    </thead>
                    <tbody>
                      {
                        data_ML !== null &&
                        data_ML.res.map((item, index) => {
                          console.log(item)
                          return (
                              <tr key={index}>
                                <td>
                                  { item.SpeakerLabel }
                                </td>
                                <td>
                                  { item.StartTime }
                                </td>
                                <td>
                                  { item.EndTime }
                                </td>
                                <td>
                                  { item.TimeSeconds }
                                </td>
                                <td>
                                  { item.Transcription }
                                </td>
                              </tr>
                          )
                        })
                      }
                    </tbody>

                  </Table>
                </Col>
              </Row>
              {/* <ShowGet {}/> */}


            </Container>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={hide}>
            Close
          </Button>
        </Modal.Footer>
      </Modal>
  )
}

export default PopOver