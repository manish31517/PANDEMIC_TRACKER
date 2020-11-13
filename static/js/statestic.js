 var $reports = $('#reports');
async function fetchCovidData()
{
  let response = await fetch('https://api.covid19india.org/data.json');
  let reports = await response.json();
  var statecount=(reports['statewise']).length;
  console.log(reports['statewise'][0]['state'])
  total=reports['statewise'][0]['confirmed'];
  active=reports['statewise'][0]['active'];
  recover=reports['statewise'][0]['recovered'];
  deaths=reports['statewise'][0]['deaths'];
 
  document.getElementById('tt').innerHTML=total;  
 document.getElementById('recover').innerHTML=recover;  
 document.getElementById('active').innerHTML=active;  
 document.getElementById('death').innerHTML=deaths;  
 
  var i =1;
while(i<(statecount-2)){
    $reports.append('<tr scope="row"><td>'+reports['statewise'][i]['state']+'</td><td>'+reports['statewise'][i]['confirmed']+'</td><td>'+reports['statewise'][i]['active']+'</td><td>'+reports['statewise'][i]['recovered']+'</td><td>'+reports['statewise'][i]['deaths']+'</td><td>'+reports['statewise'][i]['lastupdatedtime']+'</td></tr>')
 i++;  
}
  
}

fetchCovidData();