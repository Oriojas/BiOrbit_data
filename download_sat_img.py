import requests


class downloadSatImg:

    def __init__(self, coord: list, token: str):
        self.coord = coord
        self.token = token

    def img(self):
        response = requests.post('https://services.sentinel-hub.com/api/v1/process',
                                 headers={"Authorization": f"Bearer {self.token}"},
                                 json={
                                     "input": {
                                         "bounds": {
                                             "bbox": [
                                                        self.coord[0],
                                                        self.coord[1],
                                                        self.coord[2],
                                                        self.coord[3]
                                                    ]
                                         },
                                         "data": [{
                                             "type": "sentinel-2-l2a"
                                         }]
                                     },
                                     "evalscript": """
            //VERSION=3
        
            function setup() {
              return {
                input: ["B02", "B03", "B04"],
                output: {
                  bands: 3
                }
              };
            }
        
            function evaluatePixel(
              sample,
              scenes,
              inputMetadata,
              customData,
              outputMetadata
            ) {
              return [2.5 * sample.B04, 2.5 * sample.B03, 2.5 * sample.B02];
            }
            """
         })

        print(response)

        return response.text

