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
  name: deuitdaging-dev
  labels:
    app: deuitdaging-dev
spec:
  replicas: 1
  selector:
    matchLabels:
      app: deuitdaging-dev
  template:
    metadata:
      labels:
        app: deuitdaging-dev
    spec:
      containers:
      - name: deuitdaging-dev
        image: gcr.io/GOOGLE_CLOUD_PROJECT/deuitdaging:COMMIT_SHA
        ports:
        - containerPort: 8080
---
kind: Service
apiVersion: v1
metadata:
  name: deuitdaging-dev
spec:
  selector:
    app: deuitdaging-dev
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: LoadBalancer
