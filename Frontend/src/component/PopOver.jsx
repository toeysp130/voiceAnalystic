import React from 'react';
import Button from 'react-bootstrap/Button';
import Modal from 'react-bootstrap/Modal';
import Dchart from './Dchart';
import Container from 'react-bootstrap/Container'
import ShowGet from './ShowGet';
const PopOver = ({isShow , hide}) => {

  return (
    <Modal show={isShow} onHide={hide}>
        <Modal.Header closeButton>
          <Modal.Title>RegularX & Sentiment Result</Modal.Title>
        </Modal.Header>
        <Modal.Body>
            <Container>
                <Dchart />
                <ShowGet />


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