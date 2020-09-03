function total_runs_team(){

    var team = new Array();
    var chkbox = document.getElementById('tab1');
    var selctchk = chkbox.getElementsByTagName('input');
    for ( var i=0; i<selctchk.length; i++){
      if(selctchk[i].checked){
        team.push(selctchk[i].value)
      }
    }

    var games = new Array();
    var chkbox = document.getElementById('tab2').value;
    games.push(chkbox);

    const runsScored= [];
    fetch("http://127.0.0.1:8000/runs/", {method: 'POST', headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }, body: JSON.stringify({teams: team, game: games})})
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        for(let team in data){
            runsScored.push([team,data[team]]);
        }

        Highcharts.chart("total-runs-scored",{
            chart: {
                type: "column"
            },
            title: {
                text: "Total Runs scored"
            },
            xAxis: {
                type: "category",
                title: {
                    text: "Teams Played"
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: "No. of Games Played"
                }
            },
            series: [
                {
                    colorByPoint: true,
                    name: "teams",
                    data: runsScored
                }
            ]
        });
    });
}

function top_rcb_batsmen(){

    var batsman = new Array();
    var chkbox = document.getElementById('tab3');
    var selctchk = chkbox.getElementsByTagName('input');
    for ( var i=0; i<selctchk.length; i++){
      if(selctchk[i].checked){
        batsman.push(selctchk[i].value)
      }
    }

    var runs = new Array();
    var chkbox = document.getElementById('tab4').value;
    runs.push(chkbox);

    const topBatsmen= [];
    fetch("http://127.0.0.1:8000/batsman/", {method: 'POST', headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }, body: JSON.stringify({batsmans: batsman, run: runs})})
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        for(let batsmen in data){
            topBatsmen.push([batsmen,data[batsmen]]);
        }

        Highcharts.chart("top-rcb-batsmen",{
            chart: {
                type: "bar"
            },
            title: {
                text: "Top Batsmen"
            },
            xAxis: {
                type: "category",
                title: {
                    text: "Batsmen"
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: "Runs Scored"
                }
            },
            series: [
                {
                    name: "batsmen",
                    data: topBatsmen
                }
            ]
        });
    });
}

function foreign_umpires(){

    var ump_nation = new Array();
    var chkbox = document.getElementById('tab5');
    var selctchk = chkbox.getElementsByTagName('input');
    for ( var i=0; i<selctchk.length; i++){
      if(selctchk[i].checked){
        ump_nation.push(selctchk[i].value)
      }
    }

    const umpires= [];
    fetch("http://127.0.0.1:8000/umpires/", {method: 'POST', headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }, body: JSON.stringify(ump_nation)})
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        for(let ump in data){
            umpires.push([ump,data[ump]]);
        }

        Highcharts.chart("foreign-umpires",{
            chart: {
                type: "column"
            },
            title: {
                text: "Foreign Umpires"
            },
            xAxis: {
                type: "category",
                title: {
                    text: "Umpires"
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: "Countries"
                }
            },
            series: [
                {
                    colorByPoint: true,
                    name: "No. of umpires",
                    data: umpires
                }
            ]
        });
    });
}

function teams_seasons_games(){

    // Seasons
    var seasons = new Array();
    var chkbox = document.getElementById('tab6');
    var selctchk = chkbox.getElementsByTagName('input');
    for ( var i=0; i<selctchk.length; i++){
      if(selctchk[i].checked){
        seasons.push(selctchk[i].value)
      }
    }

    console.log(seasons)

    // Teams

    var teams = new Array();
    var chbox = document.getElementById('tab7');
    var selctch = chbox.getElementsByTagName('input');
    for ( var i=0; i<selctch.length; i++){
      if(selctch[i].checked){
        teams.push(selctch[i].value)
      }
    }

    console.log(teams)
    
    const processed_json = [];
    fetch("http://127.0.0.1:8000/seasons/", {method: 'POST', headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
              }, body: JSON.stringify({season: seasons, team: teams})})
    .then(function(resp){
        return resp.json();
    })
    .then(function(data){
        for(let year in data){
            var teamSeason= {};
            teamSeason["name"] = year;
            teamSeason["data"] = Object.entries(data[year]);
            processed_json.push(teamSeason);
        }
        Highcharts.chart("team-games-season",{
            chart: {
                type: "column"
            },
            title: {
                text: "Games played by Teams by Season"
            },
            xAxis: {
                type: "category",
                title: {
                    text: "Teams"
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: "Number of Games Played"
                }
            },
            plotOptions: {
                column: {
                    stacking: 'number'
                }
            },
            series: processed_json
        });   
    });
}

// total_runs_team();
// top_rcb_batsmen();
// foreign_umpires();
// teams_seasons_games();