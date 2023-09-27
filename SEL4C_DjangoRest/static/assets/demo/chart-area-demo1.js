// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Area Chart Example
var ctx = document.getElementById("myAreaChart");
var activity_labels = ctx.getAttribute("data-labels");
var activity_deliveries = ctx.getAttribute("data-data")
activity_labels = JSON.parse(activity_labels);
activity_deliveries = JSON.parse(activity_deliveries);

var myLineChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: activity_labels,
    datasets: [{
      label: "Entregables",
      lineTension: 0.3,
      backgroundColor: "rgba(213,184,255,1)",
      borderColor: "rgba(159,90,253,1)",
      pointRadius: 5,
      pointBackgroundColor: "rgba(90,34,139,1)",
      pointBorderColor: "rgba(191,85,236,1)",
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(140,20,252,1)",
      pointHitRadius: 50,
      pointBorderWidth: 2,
      data: activity_deliveries,
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'date'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 7
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 500,
          maxTicksLimit: 5
        },
        gridLines: {
          color: "rgba(0, 0, 0, .125)",
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
