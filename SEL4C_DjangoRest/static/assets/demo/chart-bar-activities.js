// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var activity_labels = ctx.getAttribute("data-labels");
var activity_deliveries = ctx.getAttribute("data-data")
activity_labels = JSON.parse(activity_labels);
activity_deliveries = JSON.parse(activity_deliveries);
var myLineChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: activity_labels,
    datasets: [{
      label: "Entregables",
      backgroundColor: "rgba(90,34,139,1)",
      borderColor:  "rgba(90,34,139,1)",
      data: activity_deliveries
    }],
  },
  options: {
    scales: {
      xAxes: [{
        time: {
          unit: 'actividad'
        },
        gridLines: {
          display: false
        },
        ticks: {
          maxTicksLimit: 6
        }
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 500,
          maxTicksLimit: 5
        },
        gridLines: {
          display: true
        }
      }],
    },
    legend: {
      display: false
    }
  }
});
