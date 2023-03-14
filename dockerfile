FROM pypy:latest
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r env_packages.txt
CMD python inventory.py