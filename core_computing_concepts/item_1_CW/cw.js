let iteratNum = 1;
let graphNum = 'first';


function changeToNext()
{
    document.getElementById('graph').src = `./images/${graphNum}-graph/${graphNum}_graph-${iteratNum}.png`;
    if (iteratNum === 10)
    {
        iteratNum = 0;
    }
    else
    {
        iteratNum += 1;
    }
}


function changeGraph()
{
    if (graphNum === 'first')
    {
        graphNum = 'second';
    } 
    else
    {
        graphNum = 'first';
    }
    iteratNum = 0;
    changeToNext();
}