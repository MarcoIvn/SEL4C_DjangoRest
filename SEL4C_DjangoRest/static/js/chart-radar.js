document.addEventListener("DOMContentLoaded", function() {

  var Chart1Data1 = document.getElementById("radarChart1").getAttribute("data-profile_results1");
  var Chart1Data2 = document.getElementById("radarChart1").getAttribute("data-profile_results2");
  var Chart2Data1 = document.getElementById("radarChart2").getAttribute("data-ecomplexity_results1");
  var Chart2Data2 = document.getElementById("radarChart2").getAttribute("data-ecomplexity_results2");

  console.log(Chart1Data1.pop())
  console.log(Chart1Data2.pop())
  console.log(Chart2Data1.pop())
  console.log(Chart2Data2.pop())
  
  var chartOptions = {
    scale: {
      angleLines: {
        display: true,
      },
      ticks: {
        suggestedMin: 0, // Valor mínimo del eje
        suggestedMax: 5, // Valor máximo del eje (ajústalo según tus necesidades)
      },
    },
  };

  var marksData1 = {
      labels: ["Motivación", "Perseverancia y resilencia", 
      "Tolerancia a la incertidumbre, ambigüedad y dominio del estrés", "Planeación estrategica", 
      "Comunicación y persuación", "Movilizar personas","Trabajo colaborativo","Implicación social", 
      "Empatía", "Identificación de problematicas sociales/ambientales", "Orientación a la sostenibilidad",
    "Sentido Ético", "Creatividad", "Alfabetización economica y financiera", "Valoración de ideas, resultados e impactos en el ambiente y las personas",
  "Aprendizaje y adaptibilidad","Gestión de recursos limitados para proyectos sociales"],
      datasets: [{
          label: "Cuestionario Inicial",
          backgroundColor: "rgba(200,0,0,0.2)",
          data: Chart1Data1,
      }, {
          label: "Cuestionario Final",
          backgroundColor: "rgba(0,0,200,0.2)",
          data: Chart1Data2,
      }]
  };

  var marksData2 = {
    labels: ["1", "2", "3", "4"],
    datasets: [{
        label: "Cuestionario Inicial",
        backgroundColor: "rgba(200,0,0,0.2)",
        data: Chart2Data1,
    }, {
        label: "Cuestionario Final",
        backgroundColor: "rgba(0,0,200,0.2)",
        data: Chart2Data2,
    }]
};

  var radarChart1 = new Chart(document.getElementById("radarChart1"), {
    type: 'radar',
    data: marksData1,  // Define tus datos para la primera gráfica
    options: chartOptions  // Opciones personalizadas para la primera gráfica si es necesario
  });

  var radarChart2 = new Chart(document.getElementById("radarChart2"), {
      type: 'radar',
      data: marksData2,  // Define tus datos para la segunda gráfica
      options: chartOptions  // Opciones personalizadas para la segunda gráfica si es necesario
  });

  
});
