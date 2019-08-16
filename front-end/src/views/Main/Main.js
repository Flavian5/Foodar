import React, { Component } from 'react';
import Survey from '../../components/Survey/Survey';

class MainPage extends Component {

    render() {
        return (
            <div className="main-page-container">
                <div className="flex-box" style={{height: '100%'}}>
                    <div style={{flex: .3}}>
                        <div style={{textAlign: 'center', paddingTop: 50}}>
                            <div style={{paddingLeft: 30, marginBottom: 50}}>
                                <img style={{width: 250}} src={"/images/logo_white.png"}/>
                            </div>
                            <div>
                                <img style={{width: 130}} src={"/images/survey_char.png"}/>
                            </div>
                        </div>
                    </div>
                    <div style={{top: 30, paddingLeft: 30, flex: .7, alignItems:'center', display: 'flex'}}>
                        <Survey/>
                    </div>
               </div>
            </div>
        );
    }
}

export default MainPage;