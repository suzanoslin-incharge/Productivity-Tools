// Revised Lucid template rules, given by Suzan Oslin on 2026-11-02.
// Saved as given, with one correction (Exception Path / Loop Back width, noted below). The CSV does not need them. See section 4.5 of lucidchart-integration.md.

const styleRules = {
  shapes: {
    "Start": {
      fillColor: "#9bb89d",
      lineColor: "#4c535d",
      lineWidth: 3,
      strokeStyle: "solid",
      textColor: "#17324d"
    },
    "Final": {
      fillColor: "#4c535d",
      lineColor: "#4c535d",
      lineWidth: 3,
      strokeStyle: "solid",
      textColor: "#ffffff"
    },
    "Manual": {
      fillColor: "#d6e9ff",
      lineColor: "#005fcc",
      lineWidth: 3,
      strokeStyle: "solid",
      textColor: "#17324d"
    },
    "Manual Review": {
      fillColor: "#d6e9ff",
      lineColor: "#005fcc",
      lineWidth: 3,
      strokeStyle: "solid",
      textColor: "#17324d"
    },
    "Automated": {
      fillColor: "#cdcddb",
      lineColor: "#553f6a",
      lineWidth: 3,
      strokeStyle: "solid",
      textColor: "#17324d"
    },
    "System Decision": {
      fillColor: "#cdcddb",
      lineColor: "#553f6a",
      lineWidth: 3,
      strokeStyle: "solid",
      textColor: "#17324d"
    },
    "TBD": {
      fillColor: "#f6b6a6",
      lineColor: "#b83280",
      lineWidth: 3,
      strokeStyle: "dashed",
      textColor: "#17324d"
    },
    "Storage": {
      fillColor: "#ffffff",
      lineColor: "#3a414a",
      lineWidth: 3,
      strokeStyle: "solid",
      textColor: "#17324d"
    },
    "Exception Path / Loop Back": {
      fillColor: "transparent",
      lineColor: "#4c535d",
      lineWidth: 3, // corrected from 4 to 3 by Suzan Oslin, 2026-11-02
      strokeStyle: "dashed",
      textColor: "#17324d"
    },
    "Termination": {
      fillColor: "#4c535d",
      lineColor: "#4c535d",
      lineWidth: 3,
      strokeStyle: "solid",
      textColor: "#ffffff"
    }
  },

  connectors: {
    "Main Flow": {
      lineColor: "#4c535d",
      lineWidth: 3,
      strokeStyle: "solid"
    },
    "Exception Path": {
      lineColor: "#4c535d",
      lineWidth: 3,
      strokeStyle: "dashed"
    },
    "Loop Back": {
      lineColor: "#4c535d",
      lineWidth: 3,
      strokeStyle: "dashed"
    }
  },

  swimlanes: {
    header: {
      fillColor: "#007aff",
      lineColor: "#3a414a",
      lineWidth: 1,
      textColor: "#ffffff"
    },
    lanes: [
      { fillColor: "#fdf5f5" },
      { fillColor: "#f5fbf7" },
      { fillColor: "#f5f9fd" }
    ]
  },

  statusOverlays: {
    "Unconfirmed": {
      fillColor: "#feeb89",
      preserveBaseLineColor: true,
      preserveBaseLineWidth: true
    }
  },

  text: {
    font: "Inter",
    size: 10,
    color: "#17324d"
  },

  key: {
    editable: true,
    useRepresentativeShapes: true,
    preserveExactLabels: true,
    preserveExactStyles: true
  },

  validation: {
    textContrast: true,
    textOverflow: true,
    blockOverlap: true,
    disconnectedEndpoint: true,
    lineThroughBlock: true,
    inefficientConnector: true,
    editableOutput: true
  }
};

const themeInput = {
  displayName: "Finalized Template Rules",
  canvasColor: "#ffffff",
  font: "Inter",
  roles: {
    default:   styleRules.shapes["Storage"],
    primary:   styleRules.shapes["Manual"],
    secondary: styleRules.shapes["Automated"],
    accent:    styleRules.shapes["Unconfirmed"] ?? {
      fillColor: "#feeb89",
      lineColor: "#005fcc",
      lineWidth: 3,
      strokeStyle: "solid",
      textColor: "#17324d"
    },
    highlight: styleRules.shapes["TBD"],
    success:   styleRules.shapes["Start"],
    error:     styleRules.shapes["Final"]
  },
  lineStyle: {
    lineColor: "#4c535d",
    lineWidth: 3,
    strokeStyle: "solid",
    textColor: "#17324d"
  },
  defaultTextStyle: styleRules.text,
  defaultLineStyle: {
    shape: "elbow",
    lineColor: "#4c535d",
    lineWidth: 3,
    strokeStyle: "solid",
    textAreaOutline: "none",
    textStyle: styleRules.text
  }
};
