# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

apiVersion: apps/v1
kind: Deployment
metadata:
  name: de-uitdaging-deployment-gclb
  labels:
    app: de-uitdaging-deployment-gclb
spec:
  replicas: 1
  selector:
    matchLabels:
      app: de-uitdaging-deployment-gclb
  template:
    metadata:
      labels:
        app: de-uitdaging-deployment-gclb
    spec:
      containers:
      - name: de-uitdaging-deployment
        image: gcr.io/GOOGLE_CLOUD_PROJECT/de-uitdaging:COMMIT_SHA
        ports:
        - containerPort: 8080
---
kind: Service
apiVersion: v1
metadata:
  name: de-uitdaging-service-gclb
spec:
  selector:
    app: de-uitdaging-deployment-gclb
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 5000
  type: NodePort
---
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: de-uitdaging-ingress-gclb
spec:
  backend:
    serviceName: de-uitdaging-service-gclb
    servicePort: 5000
