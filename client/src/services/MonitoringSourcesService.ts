/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { MonitoringSource } from '../models/MonitoringSource';
import type { MonitoringSourceMainData } from '../models/MonitoringSourceMainData';
import type { OsintView } from '../models/OsintView';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class MonitoringSourcesService {
    /**
     * Create Monitoring Source
     * @param requestBody
     * @param authorization
     * @returns MonitoringSource Successful Response
     * @throws ApiError
     */
    public static createMonitoringSource(
        requestBody: MonitoringSourceMainData,
        authorization?: (string | null),
    ): CancelablePromise<MonitoringSource> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/monitoring-sources',
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Monitoring Sources By User
     * @param limit
     * @param offset
     * @param authorization
     * @returns MonitoringSource Successful Response
     * @throws ApiError
     */
    public static getMonitoringSourcesByUser(
        limit: number = 100,
        offset?: number,
        authorization?: (string | null),
    ): CancelablePromise<Array<MonitoringSource>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/monitoring-sources',
            headers: {
                'authorization': authorization,
            },
            query: {
                'limit': limit,
                'offset': offset,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Get Monitoring Source Views
     * @param id
     * @param authorization
     * @returns OsintView Successful Response
     * @throws ApiError
     */
    public static getMonitoringSource(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<Array<OsintView>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/monitoring-sources/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Update Monitoring Source
     * @param id
     * @param requestBody
     * @param authorization
     * @returns MonitoringSource Successful Response
     * @throws ApiError
     */
    public static updateMonitoringSource(
        id: string,
        requestBody: MonitoringSourceMainData,
        authorization?: (string | null),
    ): CancelablePromise<MonitoringSource> {
        return __request(OpenAPI, {
            method: 'PUT',
            url: '/monitoring-sources/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                422: `Validation Error`,
            },
        });
    }
    /**
     * Delete Monitoring Source
     * @param id
     * @param authorization
     * @returns void
     * @throws ApiError
     */
    public static deleteMonitoringSource(
        id: string,
        authorization?: (string | null),
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/monitoring-sources/{id}',
            path: {
                'id': id,
            },
            headers: {
                'authorization': authorization,
            },
            errors: {
                422: `Validation Error`,
            },
        });
    }
}
