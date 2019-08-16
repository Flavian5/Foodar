import React, { Component } from 'react';
import Card from '../../components/card/card';
import apiClient from '../../api';

class Restaurants extends Component {

    componentDidMount() {
        
    }

    render() {
        return (
            <div style={{height: '100vh', backgroundColor: '#EDEFF1', display: 'flex'}}>
                <div style={{width: 300}}>
                    <div style={{height: '100%', backgroundColor: 'white'}}>
                        <div>
                            <div style={{textAlign: 'center', paddingTop: 20}}>
                                <img style={{width: 220}} src={'/images/logo.png'}/>
                            </div>
                            <div style={{fontSize: 20, color: '#616376', fontWeight: 500, marginTop: 40}}>
                                <p style={{paddingLeft: 20}}>My Profile</p>
                                <p style={{paddingLeft: 20}}>History</p>
                                <hr style={{borderTop: '3px solid #efefef'}}/>
                                <p style={{paddingLeft: 20}}>Preferences</p>
                                <p style={{color:'#E67D3F',background: 'linear-gradient(90deg, rgba(249,225,209,1) 0%, rgba(255,255,255,1) 100%)', padding: '20px 20px'}}>Find Place</p>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="flex-1" style={{overflow: 'auto'}}>
                    <div style={{height: 60, backgroundColor: '#8D6C6C', display: 'flex', alignItems: 'center', paddingLeft: 20}}>
                        <input placeholder="Search" style={{width: 300, borderRadius: 50, padding: '10px 20px'}}/>
                    </div>
                    <div style={{padding: '5px 40px'}}>
                        <p style={{fontSize: 30, color: '#977B7B', fontWeight: 500}}>Restaurants</p>
                        <Card/>
                    </div>
                </div>
            </div>
        );
    }
}

export default Restaurants;